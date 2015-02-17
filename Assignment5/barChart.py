import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')

    '''Reads data from csv files as rows'''
    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)

    '''Assigns first row of each csv file to a "header" variable and moves on to the second row.'''
    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    artist_names = []
    '''Creates list of every decade from 1900 to 2020, and sets up dictionary assigning the value of every decade 0'''
    decades = range(1900,2020, 10)
    decade_dict = {}
    for decade in decades:
        decade_dict[decade] = 0
    
    '''Extracting names from each row in artists_rows and appending them to list artist_names'''
    for artist_row in artists_rows:
        if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row #Assigns each index in artist_row to a variable
        artist_names.append(name)
    '''Checking which decade each album was released in'''
    for album_row  in albums_rows:
        if not album_row:
            continue
        if len(album_row) == 5: 
            artist_id, album_id, album_name, year, popularity = album_row
        else: 
            print "error with row %s" % album_row

        '''For every decade, if the year the album was released is in that decade, add 1 to that decade's value in the dictionary'''
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break
    '''Setting x-values to be the decades from 1900 to 2020 and y-values to be a list of values from decade_dict'''
    x_values = decades
    y_values = [decade_dict[d] for d in decades]
    return x_values, y_values, artist_names



def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData()
    '''Plots data returned from function getBarChartData'''
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10) #gives us bars with x_vals on the x-axis, y-vals on the y-axis, and a width of 10 units
    '''Sets bar chart labels'''
    ax.set_xlabel('decades')
    ax.set_ylabel('number of albums')
    ax.set_title('Totals for ' + ', '.join(artist_names)) #Sets title with names from the artist_names list separated by commas
    plt.show()

if __name__ == '__main__':
    getBarChartData()
    plotBarChart()
    
