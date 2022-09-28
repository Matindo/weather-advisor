export const weatherMixin = {
  data: function () {
    return {
      apiKey: 'ed0b2d87cc61572f8ae096b3700e8d28',
      weatherData: {
        city: '', icon: '', description: '', temp: '', humidity: '', wind: '', status: ''
      }
    }
  },
  methods: {
    fetchCityWeather: function (city) {
      fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${this.apiKey}`).then((response) => response.json()).then((data) => {
        this.processWeather(data)
      })
    },
    fetchCoordinateWeather: function (coordinates) {
      fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${coordinates.lat}&lon=${coordinates.lon}&units=metric&appid=${this.apiKey}`).then((response) => response.json()).then((data) => {
        this.processWeather(data)
      })
    },
    processWeather: function (data) {
      const { name } = data
      const { icon, description } = data.weather[0]
      const { temp, humidity } = data.main
      const { speed } = data.wind
      this.weatherData.city = 'Weather in ' + name
      this.weatherData.icon = 'https://openweathermap.org/img/wn/' + icon + '.png'
      this.weatherData.description = description
      this.weatherData.temp = temp + '⁰C'
      this.weatherData.humidity = 'Humidity: ' + humidity + '%'
      this.weatherData.wind = 'Wind Speed: ' + speed + 'km/h'
      this.weatherData.status = 'ready'
    }
  }
}
