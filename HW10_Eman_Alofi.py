def main():
    wdir10 ='/Users/ealofi3/icloud Drive/Documents/good_data'
    wdir_bad_data = '/Users/ealofi3/icloud Drive/Documents/bad_data'
    wdir_bad_fields = '/Users/ealofi3/icloud Drive/Documents/bad_field'

    print("Good data")
    _ = Repository(wdir10)

    print("\nBad Data")
    print("--> should report student with unknown major, grade for unknown student, and grade for unknown instructor")
    _ = Repository(wdir_bad_data)

    print("\nBad Fields\n")
    print("should report bad student, grade, instructor feeds")
    _ = Repository(wdir_bad_fields)

    print("\nNon-existent Data Directory\n")
    _ = Repository("Not A Directory")
