e.passwd = r.rsaFun(e.passwd)

rsaFun: function(e) {
    var t = "ab86b6371b5318aaa1d3c9e612a9f1264f372323c8c0f19875b5fc3b3fd3afcc1e5bec527aa94bfa85bffc157e4245aebda05389a5357b75115ac94f074aefcd",
    n = "10001",
    a = Q.crypto.rsa.RSAUtils.getKeyPair(n, "", t),
    i = Q.crypto.rsa.RSAUtils.encryptedString(a, encodeURIComponent(e)).replace(/\s/g, "-");
    return i
}

f.getKeyPair = function(a, b, c) {
    return new A(a,b,c)
};

f.encryptedString = function(a, b) {
    for (var c = [], d = b.length, e = 0; d > e; )
        c[e] = b.charCodeAt(e),
        e++;
    for (; 0 != c.length % a.chunkSize; )
        c[e++] = 0;
    var g, h, i, j = c.length, k = "";
    for (e = 0; j > e; e += a.chunkSize) {
        for (i = new t,
        g = 0,
        h = e; h < e + a.chunkSize; ++g)
            i.digits[g] = c[h++],
            i.digits[g] += c[h++] << 8;
        var l = a.barrett.powMod(i, a.e)
          , m = 16 == a.radix ? f.biToHex(l) : f.biToString(l, a.radix);
        k += m + " "
    }
    return k.substring(0, k.length - 1)
}

var A = function(a, b, c) {
    var d = f;
    this.e = d.biFromHex(a),
    this.d = d.biFromHex(b),
    this.m = d.biFromHex(c),
    this.chunkSize = 2 * d.biHighIndex(this.m),
    this.radix = 16,
    this.barrett = new g.BarrettMu(this.m)
};