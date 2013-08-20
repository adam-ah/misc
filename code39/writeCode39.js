var code39 = code39 || new Object();

code39.createLetter = function(letter){
    if(letter == '*'){
        letter = 'star';
    }
    var img = document.createElement('img');
    img.setAttribute('src', 'images/' + letter + '.png');
    img.setAttribute('class', 'code39 c' + letter);
    var td = document.createElement('td');
    td.appendChild(img);
    return td;
}

code39.createCode = function(numbers){
    var charArr = ('*' + numbers + '*').split('');
    var table = document.createElement('table');
    table.setAttribute('class', 'code39');
    var tr = document.createElement('tr');
    table.appendChild(tr);
    for(var i=0, c; c=charArr[i]; i++)
    {
        var letter = code39.createLetter(c);
        tr.appendChild(letter);
    }
    return table;
}
