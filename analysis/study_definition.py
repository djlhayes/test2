from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    #this could be women only or only alive patients or registered for 12months
    population=patients.registered_with_one_practice_between(
        "2019-02-01", "2020-02-01"
    ),
    age=patients.age_as_of(
        "2019-09-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),

    bmi=patients.most_recent_bmi(
        between=["2019-02-01", "2020-02-01"],
        minimum_age_at_measurement=18,
        include_measurement_date=True,
        date_format="YYYY-MM",
        return_expectations={
            "date": {   
                "earliest": "2019-02-01", 
                "latest": "2020-02-01"},
            "float": {
                "distribution": "normal", 
                "mean": 28, 
                "stddev": 8},
            "incidence": 0.80,
            },
        ),

    sex=patients.sex(
    return_expectations={
        "rate": "universal",
        "category": {"ratios": {"M": 0.49, "F": 0.51}},
         },
    ),

    ethnicity=patients.with_ethnicity_from_sus(
    returning="group_6",
    use_most_frequent_code=True,
    return_expectations={
            "category": {"ratios": {"1": 0.8, "2": 0.1, "3": 0.1}},
            "incidence": 0.75,
            },
    ),

    region=patients.registered_practice_as_of(
        "2020-02-01",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.2,
                    "South East": 0.2,
                },
            },
        },
    ),
)




