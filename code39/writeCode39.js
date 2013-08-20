var code39 = code39 || new Object();

code39.createLetter = function(letter){
    var div = document.createElement('div');
    if(letter == '*'){
        letter = 'star';
    }
    div.setAttribute('class', 'code39 c' + letter);
    return div;
}

code39.createCode = function(numbers){
    var charArr = ('*' + numbers + '*').split('');
    var parent = document.createElement('div');
    charArr.forEach(function(c){
        var letter = code39.createLetter(c);
        parent.appendChild(letter);
    });
    var close = document.createElement('div');
    close.setAttribute('class', 'clear');
    parent.appendChild(close);
    return parent;
}
