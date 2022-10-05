# Import
from fastapi import APIRouter, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import pandas as pd

# Local Variables
from src.routes.soccer import crud
from src.routes.soccer import schemas
from src.database.database import Base, SessionLocal, engine

# APIRouter creates path operations for item module
router = APIRouter(
    prefix="/Soccer",
    tags=["Soccer"],
    responses={404: {"description": "Not found"}},
)

# db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/Registration/")
def get_all_registration(db: Session = Depends(get_db)):
    return crud.get_all_registrations(db)

@router.get("/Match/")
def get_all_matches(db: Session = Depends(get_db)):
    return crud.get_all_matches(db)

@router.delete("/Registration/")
def delete_all_registration(db: Session = Depends(get_db)):
    return crud.delete_all_registrations(db)

@router.delete("/Match/")
def delete_all_matches(db: Session = Depends(get_db)):
    return crud.delete_all_matches(db)
    
@router.post("/Result/")
def create_registration(
    registrations_text, matches_text, db: Session = Depends(get_db)
):
    # empty db
    crud.delete_all_registrations(db=db)
    crud.delete_all_matches(db=db)

    # Add to db
    registration_df = string_to_df(
        registrations_text, ["team_name", "date", "group_number"]
    )
    for _, row in registration_df.iterrows():
        crud.create_registration(
            db=db, team_name=row[0], date=row[1], group_number=row[2]
        )
        
    matches_df = string_to_df(
        matches_text, ['team_1_name','team_2_name','team_1_score','team_2_score']
    )
    print(matches_df)
    for _, row in matches_df.iterrows():
        crud.create_match(
            db=db,
            team_1_name=row[0],
            team_2_name=row[1],
            team_1_score=row[2],
            team_2_score=row[3],
        )

    # get results
    res =  get_final_ranking_df(registration_df, matches_df).to_dict(orient='records')
    return res


def string_to_df(input_str, col_names):
    rows = input_str.split('\n')
    res = []
    for row in rows:
        res.append(row.split(" "))
    return pd.DataFrame(data=res, columns=col_names).dropna()


def get_final_ranking_df(registration_df, matches_df):
    
    # format date
    registration_df['date'] = pd.to_datetime(registration_df['date'], format="%d/%m")
    
    # split df, each row has a unique team\
    matches_df_dup = matches_df.copy()
    matches_df_dup=matches_df_dup.drop('team_1_name', axis=1).rename(
        columns={
            'team_2_name': 'team_name',
            'team_1_score': 'other_team_score',
            'team_2_score': 'team_score'
        })
    matches_df=matches_df.drop('team_2_name', axis=1).rename(
        columns={
            'team_1_name': 'team_name',
            'team_2_score': 'other_team_score',
            'team_1_score': 'team_score'
        })

    matches_df=matches_df.append(matches_df_dup)
    
    # count scores for each team
    matches_df=matches_df.dropna()
    matches_df_scored = calculate_scores(matches_df)
    matches_df_scored = matches_df_scored.astype({'team_score':'int'})
    
    # group by team
    df_grouped = matches_df_scored.groupby('team_name').sum().reset_index()

    # give grp & join dates
    df = pd.merge(df_grouped,registration_df,left_on='team_name',right_on='team_name')
    
    # rank
    return df.sort_values(['normal_score', 'team_score', 'alternate_score', 'date'],
               ascending=[False, False, False,
                          True]).groupby('group_number').head(4)
    

def calculate_scores(df):

    # normal score
    df['normal_score'] = df.apply(lambda x: 3
                           if x['team_score'] > x['other_team_score'] else 1
                           if x['team_score'] == x['other_team_score'] else 0,
                           axis=1)
    
    # alt scores
    df['alternate_score'] = df.apply(lambda x: 5
                           if x['team_score'] > x['other_team_score'] else 3
                           if x['team_score'] == x['other_team_score'] else 1,
                           axis=1)
    
    return df