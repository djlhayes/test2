from cohortextractor import (
    StudyDefinition, 
    patients, 
    codelist, 
    codelist_from_csv, 
    Measure  
    # NOQA
)

#start_date = "2019-02-01"
#end_date = "2020-02-01"

#index_date=start_date,

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

    #this could be women only or only alive patients or registered for 12months
    #make new study population of 1000 women of reproductive age

    population=patients.registered_with_one_practice_between(
       "2019-02-01", "2020-02-01"
    ),
  
    #population=patients.satisfying(
     #   "practice AND (sex = 'F')",
    #)

 
    age=patients.age_as_of(
        "2019-09-01",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),

    age_cat=patients.categorised_as(
        {
            "0":"DEFAULT",
            "0-4": """ age >= 0 AND age < 5""",
            "5-14": """ age >= 5 AND age < 15""",
            "15-24": """ age >= 15 AND age < 25""",
            "25-34": """ age >= 25 AND age < 35""",
            "35-44": """ age >= 35 AND age < 45""",
            "45-54": """ age >= 45 AND age < 55""",
            "55-64": """ age >= 55 AND age < 65""",
            "65-74": """ age >= 65 AND age < 75""",
            "75+": """ age >= 75 AND age < 120""",
        },
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0,
                    "0-4": 0.12, 
                    "5-14": 0.11,
                    "15-24": 0.11,
                    "25-34": 0.11,
                    "35-44": 0.11,
                    "45-54": 0.11,
                    "55-64": 0.11,
                    "65-74": 0.11,
                    "75+": 0.11,
                }
            },
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

    practice=patients.registered_practice_as_of(
        "2020-02-01",
        returning="pseudo_id",
        return_expectations={"int": {"distribution": "normal",
                                     "mean": 25, "stddev": 5}, "incidence": 1}
    ),

    admitted=patients.admitted_to_hospital(
        returning="binary_flag",
        between=["2019-02-01", "2020-02-01"],
        return_expectations={"incidence": 0.1},
    ),
    
    #stp=patients.registered_practice_as_of(
     #   "2020-02-01"
      #  returning="stp_code",
       # return_expectations={
        #    "category": {"ratios": {"stp1": 0.1, "stp2": 0.2, "stp3": 0.3}},
         #   "incidence": 1,
        #},
    #),

)

#Measures

measures = [
    
    Measure(id="admissions_by_age",
            numerator="admitted",
            denominator="population",
            group_by=["age"],
            ),

    Measure(id="admissions_by_age_cat",
            numerator="admitted",
            denominator="population",
            group_by=["age_cat"],
            ),        
]


#needs Measure added to import statements at top 
#small_number_suppressions to replace values <5 with zero

