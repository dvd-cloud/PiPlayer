import vlc


class MusicPlayer:
    """Audio player for PiPlayer using VLC/libVLC instead of pygame.mixer."""

    def __init__(self):
        # VLC handles MP3 decoding and audio output.
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.current_file = None
        self.playing = False
        self.paused = False

    def load(self, filename):
        media = self.instance.media_new(filename)
        self.player.set_media(media)
        self.current_file = filename
        self.playing = False
        self.paused = False

    def play(self):
        result = self.player.play()
        # libVLC may return -1 on an immediate failure.
        if result == -1:
            print("VLC: afspelen mislukt:", self.current_file)
            self.playing = False
            return

        self.playing = True
        self.paused = False

    def pause(self):
        self.player.set_pause(1)
        self.playing = False
        self.paused = True

    def resume(self):
        self.player.set_pause(0)
        self.playing = True
        self.paused = False

    def stop(self):
        self.player.stop()
        self.playing = False
        self.paused = False

    def toggle(self):
        if self.playing:
            self.player.set_pause(1)
            self.playing = False
            self.paused = True
        elif self.paused:
            self.player.set_pause(0)
            self.playing = True
            self.paused = False
        else:
            self.player.play()
            self.playing = True
            self.paused = False

    def get_position(self):
        """Return current playback position in whole seconds."""
        position_ms = self.player.get_time()
        if position_ms < 0:
            return 0
        return position_ms // 1000

    def is_ended(self):
        """Return True when VLC has reached the end of the current track."""
        return self.player.get_state() == vlc.State.Ended

    def release(self):
        self.player.stop()
        self.player.release()
        self.instance.release()
