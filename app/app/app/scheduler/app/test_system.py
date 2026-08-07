from app.story_generator import create_story
from app.provider_manager import (
    get_primary_provider,
    get_backup_provider
)

print("=== TINY TAILS TEST ===")

story = create_story()

print("\nTITLE:")
print(story["title"])

print("\nSCENES:")
for scene in story["scenes"]:
    print(scene["description"])

print("\nPRIMARY VIDEO PROVIDER:")
print(get_primary_provider())

print("\nBACKUP VIDEO PROVIDER:")
print(get_backup_provider())

print("\nSYSTEM TEST COMPLETE")
