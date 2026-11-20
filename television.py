class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Set the default television values
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        # Turn the television on or off
        self.__status = not self.__status

    def mute(self):
        # Mute or unmute the television
        self.__muted = not self.__muted

    def channel_up(self):
        # Increase the channel only when the television is on
        if self.__status:
            # Move to the next channel if below the maximum
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                # Return to the minimum channel
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        # Decrease the channel only when the television is on
        if self.__status:
            # Move to the previous channel if above the minimum
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                # Return to the maximum channel
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        # Increase the volume only when the television is on
        if self.__status:
            # Unmute the television when adjusting the volume
            self.__muted = False

            # Increase the volume if below the maximum
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        # Decrease the volume only when the television is on
        if self.__status:
            # Unmute the television when adjusting the volume
            self.__muted = False

            # Decrease the volume if above the minimum
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        # Display the minimum volume when the television is muted
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            # Display the current volume when not muted
            volume = self.__volume

        # Return the television's current information
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
