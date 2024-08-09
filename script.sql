-- Create the database
CREATE DATABASE HealthcareApp;
USE HealthcareApp;

-- Create a Users table
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL
);

-- Create a DailyActivities table
CREATE TABLE DailyActivities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    Date DATE,
    NutrientIntake VARCHAR(255),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create a HealthConditions table
CREATE TABLE HealthConditions (
    ConditionID INT AUTO_INCREMENT PRIMARY KEY,
    ConditionName VARCHAR(255) NOT NULL
);

-- Create a UserHealthConditions table
CREATE TABLE UserHealthConditions (
    UserID INT,
    ConditionID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ConditionID) REFERENCES HealthConditions(ConditionID),
    PRIMARY KEY (UserID, ConditionID)
);

-- Create a FoodRecommendations table
CREATE TABLE FoodRecommendations (
    RecommendationID INT AUTO_INCREMENT PRIMARY KEY,
    ConditionID INT,
    RecommendedFood VARCHAR(255),
    AvoidanceFood VARCHAR(255),
    FOREIGN KEY (ConditionID) REFERENCES HealthConditions(ConditionID)
);

-- Insert initial users
INSERT INTO Users (UserName, Email, Password) VALUES
('Jane', 'jane@gmail.com', 'password456');

-- Insert initial daily activities
INSERT INTO DailyActivities (UserID, Date, NutrientIntake) VALUES
(1, '2024-08-01', 'Protein: 50g, Carbs: 200g, Fats: 70g'),
(2, '2024-08-01', 'Protein: 60g, Carbs: 180g, Fats: 80g');

-- Insert initial health conditions
INSERT INTO HealthConditions (ConditionName) VALUES
('Diabetes'),
('Jaundice'),
('Hypertension');

-- Insert initial user health conditions
INSERT INTO UserHealthConditions (UserID, ConditionID) VALUES
(1, 1), -- John Doe has Diabetes
(2, 3); -- Jane Smith has Hypertension

-- Insert initial food recommendations
INSERT INTO FoodRecommendations (ConditionID, RecommendedFood, AvoidanceFood) VALUES
(1, 'Vegetables, Whole Grains, Lean Protein', 'Sugary Foods, Refined Carbs'),
(2, 'Fruits, Boiled Vegetables, Water', 'Fried Foods, Spicy Foods, Alcohol'),
(3, 'Low-Sodium Foods, Fruits, Vegetables', 'High-Sodium Foods, Processed Foods');
