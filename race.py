import tracks
from PAO import PAO
# Import some other models and see the competition.
# More than 3/4 models is discouraged for visually pleasant competitions.


cars = [PAO()] # Add your models here

cars_models = [model.get_actor_model() for model in cars]

scoreboard = tracks.newrun(cars_models)

completion_codes = [
    "", "finished", "off track", "wrong direction", "under speed limit"
]

for car in scoreboard:
    if car["completion"] == 1:
        print(
            f"car {car['car']} ({cars[car['car']-1].get_name()}) finished in {car['place']} position."
        )
    else:
        print(
            f"car {car['car']} ({cars[car['car']-1].get_name()}) did not finish with completion code {car['completion']} ({completion_codes[car['completion']]})."
        )

print(scoreboard)  