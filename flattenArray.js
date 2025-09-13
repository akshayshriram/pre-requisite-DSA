let arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

var flat = function (arr, n) {
    if(n === 0){
        return arr
    }
    return arr.reduce((acc, currVal) => {
        if(Array.isArray(currVal)){
            return acc.concat(flat(currVal, n - 1))
        }else{
            return acc.concat(currVal)
        }
    }, [])
};

console.log(flat(arr,1))
