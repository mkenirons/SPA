from flask import Flask, render_template
app = Flask(__name__)
#for rendering the pages from the template folder
@app.route('/')
def Index():
    return render_template('index.html')
	#returns the index page from the template folder
@app.route('/home')
def Home():
	return render_template('home.html')
	#returns the home page from the template folder
@app.route('/about')
def About():
	return render_template('about.html')
	#returns the about page from the template folder
@app.route('/prototype')
def Prototype():
	return render_template('prototype.html')
	#returns the prototype page from the template folder	
@app.route('/contact')
def Contact():
	return render_template('contact.html')
	#returns the contact page from the template folder	
@app.route('/map')
def Map():
	return render_template('map.html')
	#returns the map page from the template folder	
if __name__ == "__main__":
    app.run()




