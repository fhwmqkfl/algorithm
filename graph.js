/* 가로값은 인덱스, 세로값은 배열의 값
 * 세로 : n[i], n[j]에서 작은값
 * 가로 : j-i의 값
 * 이중 for문으로 각 가로*세로 값을 빈 배열에 넣고 가장 넓은 값을 구함*/

function solution(histogram) {
    var result = [];

    for (var i = 0; i < histogram.length; i++) {
        for (var j = histogram.length-1; j > i; j--) {
            result.push(Math.min(histogram[i], histogram[j])*(j-i-1))
        }
    }

    //결과값 내림차순으로 정렬
    result.sort(function(a,b) {
        return b - a;
    });

    return result.shift();
}

