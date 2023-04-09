# Import/Export Slay the Spire Runs into JSON

1. Start a run
2. Save & Quit the run
3. Navigate to your StS save folder
4. Copy and paste the full path to the save file into `export.py` and `import.py` (For an example path for Mac, open `export.py`)
5. Run `python export.py`
6. You should see a new `.json` file in your save folder.
6. Open the JSON file in your preferred editor (i.e. [JSON Editor](https://apps.apple.com/us/app/json-editor/id567740330?mt=12) for Mac)
7. Make your changes. (For examples, see `savefile.py`.)
8. Save your changes
9. Run `python import.py`
10. Continue the run

# Credits

Thanks to GoodManWEN for making [SaveTheSpire](https://github.com/GoodManWEN/SaveTheSpire). I copied and tweaked his `savefile.py`.