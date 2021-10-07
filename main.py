from Artist import Artist
from Artwork import Artwork


if __name__ == "__main__":
    print('this program puts together artists and pairs them with their artwork title.')
    print('enter artist name:')
    userArtistName = input()
    print('enter birth year for', userArtistName,':')
    userBirthYear = int(input())
    print('enter death year for', userArtistName,':', '(if alive, type "alive")')
    userDeathYear = str(input())
    print('enter title of ', userArtistName , 'artistic piece:')
    userTitle = input()
    print('enter year created:')
    userYearCreated = int(input())

    userArtist = Artist(userArtistName, userBirthYear, userDeathYear)
    newArtwork = Artwork(userTitle, userYearCreated, userArtist)

    newArtwork.printInfo()
    exit()