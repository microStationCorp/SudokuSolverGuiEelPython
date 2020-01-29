let inp = document.querySelectorAll('.form-control')
let clear = document.getElementById('clear')
let solve = document.getElementById('solve')



clear.addEventListener('click', () => {
    for (let i of inp) {
        i.value = ''
    }
})

for (let i of inp) {
    i.addEventListener('input', (e) => {
        var value = parseInt(e.data)
        if (isNaN(value)) {
            e.target.value = ''
        }
    })
}

solve.addEventListener('click', () => {
    make_board()
    let my_board = new Array()
    let row = new Array()
    for (let i of inp) {
        row.push(i.value)
        if (row.length == 9) {
            my_board.push(row)
            row = new Array()
        }
    }
    get_test(my_board)
})

async function get_test(board) {
    let data = await eel.pyFunc(board)()
    for (let i of inp) {
        if (i.value == '0') {
            i.value = data[i.name[0]][i.name[1]]
        }
    }
}


function make_board() {
    for (let i of inp) {
        if (i.value == '') {
            i.value = 0
        }
    }
}

function make_final_board(board) {

}