// Write a function last that accepts a list and returns the last element in the list.
// If the list is empty:
// In languages that have a built-in option or result type (like OCaml or Haskell), return an empty option
// In languages that do not have an empty option, just return null

const lastJS = xs => xs.length > 0 ? xs[xs.length - 1] : null

// console.log(lastJS([]))
// console.log(lastJS([1,2,3]))

// const array = [1,2,2,3,4,4,3,3]
// const counts = {}
// for (let i = 0; i < array.length; i++) {
//     counts[array[i]] = counts[array[i]] ? counts[array[i]] + 1 : 1;
//   }

// You are to write an function that takes a string as it's first paramter. This string will be a string of words.
// You are expected to then use the second parameter, which will be an integer, to find the corresponding word in the 
// given string. The first word would be represented by 0.

// Once you have the located string you are finally going to multiply by it the third provided paramater,
// which will also be an interger. You are additionally required to add a hyphen in between each word.
// Example: modifyMultiply ("This is a string",3,5) === "string-string-string-string-string"
// Since the 3rd word is 'string'(starting from 0 remember) and the third paramater indicates that it should be repeated 5 times. 
// Ex2: modifyMultiply("Is sloppiness in code caused by ignorance or apathy? I don't know and I don't care.",6 ,8) ===
// "ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance")

modifyMultiply = (str,loc,num) => {
    let output = ''
    str = str.split(' ')
    output += `${str[loc]}-`.repeat(num)
    return output.slice(0,-1)
  } 

// console.log(modifyMultiply("This is a string",3,5))

const jsMerge = (nums1, m, nums2, n) => {
    let [iOne,iTwo,iFinal] = [m - 1, n - 1, nums1.length - 1]
    while (iTwo >= 0) {
        nums1[iFinal] = nums1[iOne] >= nums2[iTwo] ? nums1[iOne] : nums2[iTwo]
        nums1[iOne] >= nums2[iTwo] ? iOne-- : iTwo--
        iFinal--
    } return nums1
}

console.log(jsMerge([0],0,[1], 1))
console.log(jsMerge(nums1 = [1,2,3,0,0,0],m = 3,nums2 = [2,5,6],n = 3))


function feast(beast, dish) {
    return beast[0] == dish[0] && beast[beast.length-1] == dish[dish.length-1]
  }

bigAvg = (arr,k) => {
    let [avg,maxAvg] = [Math.min(...arr),Math.min(...arr)]
    console.log(avg,maxAvg)
    for(let left = 0; left < arr.length-1; left++){
        console.log(left)
        right = left + k
        console.log(arr.splice(left,right))
        avg = arr.splice(left,right).reduce((a,b) => a + b) / k
        avg > maxAvg ? maxAvg = avg : ''
    } 
}
