-- Create table structure
drop table if exists two_fa;
CREATE TABLE two_fa (
user_id INT NOT NULL,
otp_code VARCHAR(6) NOT NULL,
created_date TIMESTAMP NOT NULL
);

-- Insert data into table
INSERT INTO two_fa (user_id, otp_code, created_date) VALUES
(1, '123425', '2022-01-01 00:00:00'),
(2, '678490', '2022-02-01 00:00:00'),
(3, '245680', '2022-03-01 00:00:00'),
(4, '365912', '2022-04-01 00:00:00'),
(5, '258674', '2022-05-01 00:00:00');

-- Create table structure
drop table if exists url_conversion;
CREATE TABLE url_conversion (
input_url Text NOT NULL,
output_url Text NOT NULL
);