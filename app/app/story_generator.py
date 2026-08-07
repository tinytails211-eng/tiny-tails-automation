import json
import random

ANIMALS = [
    "a little golden-brown puppy",
    "a curious orange kitten",
    "a tiny fluffy rabbit",
    "a playful baby elephant",
    "a small red panda"
]

SETTINGS = [
    "a sunny garden",
    "a magical forest",
    "a colorful village",
    "a peaceful farm",
    "a bright seaside town"
]

LESSONS = [
    "kindness",
    "helping others",
    "sharing",
    "friendship",
    "being brave"
]


def create_story():
    animal = random.choice(ANIMALS)
    setting = random.choice(SETTINGS)
    lesson = random.choice(LESSONS)

    title = f"The {animal.title()} Who Learned About {lesson.title()}"

    scenes = [
        {
            "scene": 1,
            "description": f"{animal} explores {setting} and discovers something unusual."
        },
        {
            "scene": 2,
            "description": f"{animal} meets another little animal that needs help."
        },
        {
            "scene": 3,
            "description": f"{animal} decides to help and learns about {lesson}."
        },
        {
            "scene": 4,
            "description": f"The two animals solve the problem together."
        },
        {
            "scene": 5,
            "description": f"They celebrate their friendship as the story ends happily."
        }
    ]

    return {
        "title": title,
        "lesson": lesson,
        "scenes": scenes
    }


if __name__ == "__main__":
    print(json.dumps(create_story(), indent=2))
