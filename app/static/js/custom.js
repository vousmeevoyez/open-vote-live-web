$(document).ready(function(){
    // fetch which election
    election_id = getQueryUrl()["election_id"];
    console.log(election_id);

    var socket = io.connect('http://' + document.domain + ':' + 5000 + '/stream');
    // connect first
    socket.on('connect', function(msg) {
        console.log(msg);
        // send election id to get live count for this election
        socket.emit('live_count', {election_id : election_id});
    });
    socket.on('live_count', function(msg){
        console.log(msg);
        // update vote with latest value
        var votes = msg;
        votes.forEach(update_count);
    });
});

function getQueryUrl()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

function update_count(value) {
    $('#' + value.id).text(value.votes);
}
