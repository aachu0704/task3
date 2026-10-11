
import os
import shutil

print("=" * 40)
print("       JPG FILE ORGANIZER")
print("=" * 40)

# Get the source and destination folders
source_folder = input(
    "\nEnter the path of the folder containing JPG files: "
).strip().strip('"')

destination_folder = input(
    "Enter the path of the destination folder: "
).strip().strip('"')

# Check whether the source folder exists
if not os.path.isdir(source_folder):
    print("\nError: Source folder does not exist.")

# Prevent using the same folder for both paths
elif os.path.abspath(source_folder) == os.path.abspath(
    destination_folder
):
    print("\nError: Source and destination must be different.")

else:
    # Create destination folder if needed
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    # Find and move JPG files
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if (
            os.path.isfile(source_path)
            and filename.lower().endswith(".jpg")
        ):
            destination_path = os.path.join(
                destination_folder, filename
            )

            # Avoid overwriting an existing file
            if os.path.exists(destination_path):
                print("Skipped (already exists):", filename)
                continue

            shutil.move(source_path, destination_path)
            print("Moved:", filename)
            moved_count += 1

    print("\n" + "=" * 40)
    print("AUTOMATION COMPLETED")
    print("Total JPG files moved:", moved_count)
    print("Destination:", destination_folder)
    print("=" * 40)

