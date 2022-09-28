export const locationMixin = {
  data: function () {
    return {
      longitude: '',
      lattitude: '',
      message: '',
      error: false
    }
  },
  methods: {
    getLocation: function () {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition, this.showError)
      } else {
        this.error = true
        this.message = 'Geolocation is not supported by this browser.'
      }
    },
    showPosition: function (position) {
      this.lattitude = position.coords.latitude
      this.longitude = position.coords.longitude
      this.message = 'Latitude: ' + this.lattitude + '<br>Longitude: ' + this.longitude
    },
    showError: function (error) {
      switch (error.code) {
        case error.PERMISSION_DENIED:
          this.message = 'User denied the request for Geolocation.'
          break
        case error.POSITION_UNAVAILABLE:
          this.message = 'Location information is unavailable.'
          break
        case error.TIMEOUT:
          this.message = 'The request to get user location timed out.'
          break
        case error.UNKNOWN_ERROR:
          this.message = 'An unknown error occurred.'
          break
      }
      this.error = true
    }
  }
}
