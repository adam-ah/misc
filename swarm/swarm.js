var total = 100;

var Boid = function(){
	this.x = 0;
	this.y = 0;
	this.div = $('<div class="boid">');
	this.id = Boid.count++;
	this.div.attr('id', this.id);
	var colorR = parseInt(255 * Math.random());
	var colorG = parseInt(255 * Math.random());
	var colorB = parseInt(255 * Math.random());
	var color = 'rgb(' + colorR + ',' + colorG + ',' + colorB + ')';  
	this.div.css('background-color', color);
	this.draw = function(container){
		if(!container.find('#' + this.id).length){
			this.div.appendTo(container);
		}
		this.div.css('margin-left', this.x);
		this.div.css('margin-top', this.y);
	}
}

Boid.count = 0;
Boid.speed = 7;
Boid.speedToCenter = 3;
Boid.speedToDestination = 5;
Boid.awayDistanceCheck = 30;
Boid.awaySlowdown = 5;

var Destination = function(x, y){
	this.x = x;
	this.y = y;
}

var Block = function(x, y, width, height){
	this.x = x;
	this.y = y;
	this.height = height;
	this.width = width;
	this.div = $('<div class="block">');
	this.div.attr('id', 'block');
	this.div.css('background-color', 'gray');
	this.draw = function(container){
		if(!container.find('#' + this.id).length){
			this.div.appendTo(container);
		}
		this.div.css('left', this.x);
		this.div.css('top', this.y);
		this.div.css('width', this.width);
		this.div.css('height', this.height);
	}
	this.inBlock = function(px, py){
		if(px < this.x) return false;
		if(px > this.x + this.width) return false;
		if(py < this.y) return false;
		if(py > this.y + this.height) return false;
		return true;
	}
}

function GenerateBoids(){
	var boids = [];
	for(var i = 0; i < total; i++){
		var b = new Boid();
		b.x += -50 + 100 * Math.random();
		b.y += -50 + 100 * Math.random();
		boids.push(b);
	}

	return boids;
}

function StepBoids(boids, destination, blocks){
	for(var i = 0, b; b = boids[i]; i++){
		var dCenter = StepBoidCenter(b, boids); // Get a vector center.
		var dDest = StepBoidDestination(b, destination); // Get a vector for destination.
		var dAway = StepBoidAway(b, boids); // Get a vector away from others.
		var x = dAway.x + dCenter.x + dDest.x;
		var y = dAway.y + dCenter.y + dDest.y;
		var length = Math.sqrt(x*x + y*y);
		if(length){
			x = x * Boid.speed / length; // Normalise speed.
			y = y * Boid.speed / length;
		}

		var blocked = false;
		for(var j = 0, block; block = blocks[j]; j++){
			if(block.inBlock(b.x + x, b.y + y)){
				blocked = true; // Simple 'wall' detection.
				break;
			}
		}
		if(!blocked){
			b.x += x; 
			b.y += y;
		}
	}
}

function StepBoidAway(boid, boids){
	var d = new Destination(0, 0);

	for(var i = 0, b; b = boids[i]; i++){
		if(b === boid){
			continue;
		}
		var dx = boid.x - b.x;
		var dy = boid.y - b.y;
		var dist = Math.sqrt(dx*dx + dy*dy);
		// Empirical value.
		if(dist > Boid.awayDistanceCheck){
			continue;
		}
		d.x += 2 * (boid.x - b.x);
		d.y += 2 * (boid.y - b.y);
	}

	return d;
}

function StepBoidCenter(boid, boids){
	var c = new Destination(0, 0);

	for(var i = 0, b; b = boids[i]; i++){
		c.x += b.x;
		c.y += b.y;
	}
	c.x /= boids.length;
	c.y /= boids.length;

	var x = c.x - boid.x;
	var y = c.y - boid.y;
	var length = Math.sqrt(x*x + y*y);
	if(length > Boid.speedToCenter){
		x = x * Boid.speedToCenter / length;
		y = y * Boid.speedToCenter / length;
	}

	return new Destination(x, y);
}

function StepBoidDestination(boid, destination){
	var x = -boid.x + destination.x;
	var y = -boid.y + destination.y;
	var length = Math.sqrt(x*x + y*y);
	x = x * Boid.speedToDestination / length;
	y = y * Boid.speedToDestination / length;
	return new Destination(x, y);
}

var boids = GenerateBoids();
var d = new Destination(1000,100);
var container = $('#boids');
var blocks = [new Block(500, 200, 50, 200)];
blocks[0].draw(container);

setInterval(animateBoids, 100);


function animateBoids(){
	for(var i = 0, b; b = boids[i]; i++){
		b.draw(container);
	}
	StepBoids(boids, d, blocks);
}

$(function(){
	$(document).click(function(e){
		var x = e.clientX; //  - window.innerWidth / 2;
		var y = e.clientY; //  - window.innerHeight / 2;
		d = new Destination(x, y);
	})
});
