from flask import Flask, render_template, request
import pyowm, arrow,os
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('weather.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      '''print(result["city"])
      #out["new attribute"] = 100
      #print(type(result))
      #Getting Weather Details'''
      key = os.environ['KEY']
      out = {}
      owm = pyowm.OWM(key)
      observation = owm.weather_at_place(result["city"])
      w = observation.get_weather()
      temperature = w.get_temperature('celsius')
      pressure = w.get_pressure()
      out["City"] = result["city"]
      out["humidity"] = w.get_humidity()
      out["Temperature"] = temperature['temp']
      out["Pressure"] = pressure['press']
      out["Minimum Temperature"] = temperature['temp_min']
      out["Maximum Temperature"] = temperature['temp_max']
      timestr = w.get_reference_time(timeformat='iso')
      out["Time"] = arrow.get(timestr).format('YYYY-MM-DD HH:mm:ss')
      return render_template("result.html",result = out)

if __name__ == '__main__':
   app.run(debug = True)