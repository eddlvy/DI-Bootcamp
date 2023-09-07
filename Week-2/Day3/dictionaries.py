# prices = {
#   'apple' : 2,
#   'banana' : 5,
#   'orange' :1
# }


# total = 0


# for price in prices.values():
#    total += price
# print(total)

# exercise

# Print the total duration of the playlist

playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}

playlist_total_time = 0

for duration in playlist["songs"]:
   playlist_total_time += duration["duration"]

print(playlist_total_time)
   

