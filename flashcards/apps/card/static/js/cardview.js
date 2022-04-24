(async function () {
    const deck_id = JSON.parse(document.getElementById('id').textContent);

    await fetch(
        `http://127.0.0.1:8000/deck/api/v1/${deck_id}/`
    )
        .then((response) => {
            return response.json()
        })
        .then(deck => {
            const card_text = document.getElementById('card-text')
            const card = document.getElementById('card')

            window.deck_cards = deck.cards
            const arrow_left = document.getElementById('arrow-left')
            const arrow_right = document.getElementById('arrow-right')

            let current = deck_cards[0]

            getCard(current).then((card) => {
                card_text.innerText = card.front
            })


            arrow_left.addEventListener("click", () => {
                if (current !== deck_cards[0]) {
                    current = getPreviousCard(current, deck_cards)
                    getCard(current).then((card) => {
                        card_text.innerText = card.front
                    })
                }
            })

            arrow_right.addEventListener("click", () => {
                if (current !== deck_cards[deck_cards.length - 1]) {
                    current = getNextCard(current, deck_cards)
                    getCard(current).then((card) => {
                        card_text.innerText = card.front
                    })
                }
            })

            card.addEventListener("click", () => {
                getCard(current).then((card) => {
                    if (card_text.innerText === card.front) {
                        card_text.innerText = card.back
                    } else {
                        card_text.innerText = card.front
                    }
                })
            })
        })
})();

function getNextCard(current, cards) {
    let current_card = cards.indexOf(current)
    return cards[current_card + 1]
}

function getPreviousCard(current, cards) {
    let current_card = cards.indexOf(current)
    return cards[current_card - 1]
}

async function getCard(current) {
    return await fetch(`http://127.0.0.1:8000/card/api/v1/${current}/`)
        .then((response) => {
            return response.json()
        })
}
