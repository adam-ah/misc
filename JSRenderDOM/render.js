var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

function renderHTML(html)
{
	var data = "<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'>" +
		"<foreignObject width='100%' height='100%'>" +
		html +
		"</div>" +
		"</foreignObject>" +
		"</svg>";
	var DOMURL = self.URL || self.webkitURL || self;
	var img = new Image();
	var svg = new Blob([data], {type: "image/svg+xml;charset=utf-8"});
	var url = DOMURL.createObjectURL(svg);
	img.onload = function() {
		ctx.drawImage(img, 0, 0);
		DOMURL.revokeObjectURL(url);
	};
	img.src = url;
	document.getElementById('target').appendChild(img);
}

function getImageData(url, callback)
{
	var img = document.createElement('img');
	img.setAttribute('src', 'bunny.jpg');
	img.onload = function(e){
		var imgCanvas = document.createElement('canvas');
		imgCanvas.width = img.width;
		imgCanvas.height = img.height;
		var imgCtx = imgCanvas.getContext('2d');
		imgCtx.drawImage(img, 0, 0);
		var imgData = imgCanvas.toDataURL("image/png");
		callback(imgData);
	}
}

var html = 
"<div xmlns='http://www.w3.org/1999/xhtml' style='font-size:40px'>" +
"<em>I</em> like <span style='color:white; text-shadow:0 0 2px blue;'>carrots :)</span>" +
"<br/>" +
"<img src='bunny.jpg' />";

getImageData('bunny.jpg', function(data){
	html = html.replace('bunny.jpg', data);	
	console.log(html);
	var div = document.createElement('div');
	div.innerHTML = html;
	document.body.appendChild(div);
	renderHTML(html);
});
