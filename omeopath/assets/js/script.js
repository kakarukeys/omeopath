/* Author: UserVoice
    for feedback button
*/

var uvOptions = {};
(function() {
    var uv = document.createElement('script'); uv.type = 'text/javascript'; uv.async = true;
    uv.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'widget.uservoice.com/OVQmB8TUoNg6sTR8ZJmQ.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(uv, s);
})();


/* Author: Joseph K. Myers, Wong Jiang Fung
    for input validation
*/

var vljs = new function() {
    function nwts(s) { // no white space
        return s.replace(/\s+/g, '');
    }

    function trimwts(s) { // trim white space
        return s.replace(/^\s+|\s+$/g, '');
    }

    this.number = function(s) { // any number, including exponent
        s = nwts(s) - 0;
        return isNaN(s) ? 10 : 0;
    };

    this.zip = function(s) { // zip code
        var a = nwts(s).match(/\d{5}(-?\d{4}){0,1}/g);
        return a != null && a.length ? 0 : 1;
    };

    this.tel = function(s) { // telephone, with area code + opt prefixes
        var a = s.replace(/\D+/g, '-');
        a = a.match(/(\d+-?)*(\d{3}-?){2}\d{4}/g);
        return a != null && a.length ? 0 : 2;
    };

    /* this code is copied from
    http://www.codelib.net/home/jkm/checksum.js */
    function checksum(s) { // thanks to daniel_amor@hp.com for AMEX specs
        var p = 0,
            e = 8,
            t = 0,
            c = [],
            r = 0,
            l = 0,
            i;
        if (s.length != 16) {
            t = 1;
            e = s.length == 13 && 6 || s.length == 15 && 7;
        }
        for (i = p; i < e; i++)
        r += (c[i] = s.charAt(i * 2 + t) * 2) > 9 ? Math.floor(c[i] / 10 + c[i] % 10) : c[i];
        for (i = p; i < e + t; i++) l += s.charAt(i * 2 + 1 - t) - 0;
        l += r;
        return e && l % 10 == 0;
    }

    this.cardno = function(s) {
        s = s.replace(/\D+/g, '');
        return checksum(s) ? 0 : 4;
    };

    this.text = function(s) {
        s = trimwts(s);
        return s.length ? 0 : 5;
    };

    this.words = function(s) {
        return /\s/.test(s) ? 0 : 9;
    };

    this.email = function(s) {
        a = s.match(/\S+@([-\w]+\.)+\w+/g);
        return a != null && a.length ? 0 : 6;
    };

    this.url = function(s) {
        a = s.match(/\w{2,}:\/{2}([-\w]+\.)+\w+\S*/g);
        return a != null && a.length ? 0 : 11;
    };
}();

