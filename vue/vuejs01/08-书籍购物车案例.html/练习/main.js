const app = new Vue({
    el: '#app',
    data: {
        books: [
            { id: 100, name: "java", date: 2020 - 8, price: 55.00, count: 1 },
            { id: 101, name: "cpp", date: 2020 - 9, price: 66.00, count: 1 },
            { id: 102, name: "php", date: 2020 - 10, price: 77.00, count: 1 },
            { id: 103, name: "python", date: 2020 - 11, price: 88.00, count: 1 },
            { id: 104, name: "shell", date: 2020 - 12, price: 99.00, count: 1 },
            { id: 105, name: "android", date: 2020 - 7, price: 110.00, count: 1 },
        ]
    },
    filters: {
        showPrice(price) {
            return "￥" + price.toFixed(2)
        }
    },
    methods: {
        decrement(index) {
            this.books[index].count--
        },
        increment(index) {
            this.books[index].count++
        },
        removeBook(index) {
            this.books.splice(index, 1)
        }
    },
    computed: {
        totalPrice() {
            let totalPrice = 0
            for (let i = 0; i < this.books.length; i++) {
                totalPrice += this.books[i].price * this.books[i].count
            }
            return totalPrice
        },
        totalPrice_of() {
            let totalPrice = 0
            for (let i of this.books) {
                totalPrice += i.price * i.count
            }
            return totalPrice
        },
        totalPrice_in() {
            let totalPrice = 0
            for (let i in this.books) {
                console.log(i);
                totalPrice += this.books[i].price * this.books[i].count
            }
            return totalPrice
        },
        // reduce
        totalPrice_reduce() {
            return this.books.reduce(function(preValue, book) {
                return preValue + book.price * book.count
            }, 0)

        }
    }
})