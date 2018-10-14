import lyricwikia

class LyricFinder:

    def __init__(self, lyric_length):
        self.lyric_length = lyric_length
    
    def find_lyrics(self, artist, title, progress):
        try: 
            lyrics = lyricwikia.get_lyrics(artist, title)
            lyrics = lyrics.split()
            index = int(progress*len(lyrics))
            sing_along = ' '.join(lyrics[index:(index+self.lyric_length)])
            return sing_along
        except lyricwikia.LyricsNotFound:        
            return(None)
