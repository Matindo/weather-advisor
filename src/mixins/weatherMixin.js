import moment from 'moment'

export const weatherMixin = {
  data: function () {
    return {
      apiKey: 'ed0b2d87cc61572f8ae096b3700e8d28',
      weatherData: {
        city: '', icon: '', description: '', temp: '', humidity: '', wind: '', status: '', background: ''
      },
      weatherForecast: []
    }
  },
  methods: {
    fetchCityWeather: function (city) {
      fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${this.apiKey}`).then((response) => response.json()).then((data) => {
        this.processWeather(data)
      })
    },
    fetchCityForecast: function (city) {
      this.weatherForecast.splice(0, this.weatherForecast.length)
      fetch(`https://api.openweathermap.org/data/2.5/forecast?q=${city}&units=metric&appid=${this.apiKey}`).then((response) => response.json()).then((data) => {
        this.processForecast(data)
      })
    },
    fetchCoordinateWeather: function (coordinates) {
      fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${coordinates.lat}&lon=${coordinates.lon}&units=metric&appid=${this.apiKey}`).then((response) => response.json()).then((data) => {
        this.processWeather(data)
      })
    },
    fetchCoordinateForecast: function (coordinates) {
      this.weatherForecast.splice(0, this.weatherForecast.length)
      fetch(`https://api.openweathermap.org/data/2.5/forecast?lat=${coordinates.lat}&lon=${coordinates.lon}&units=metric&appid=${this.apiKey}`).then((response) => response.json()).then((data) => {
        this.processForecast(data)
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
      this.weatherData.background = data.weather[0].main
    },
    processForecast: function (data) {
      var count
      var d = 0
      while (d < 5) {
        count = d * 8
        const dateTime = moment(data.list[count].dt_txt).format('L')
        const day = { day: d, date: dateTime, weather: [] }
        for (var j = 0; j < 8; j++) {
          day.weather.push(data.list[count])
          count += 1
        }
        d += 1
        this.weatherForecast.push(day)
      }
    }
  }
}
