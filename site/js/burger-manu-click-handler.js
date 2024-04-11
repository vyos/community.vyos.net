document.addEventListener('click', (e) => {
	const burgerMenuIcon = document.getElementById('burgerMenu')
	const closeBurgerMenuIcon = document.getElementById('closeIcon')
	const bottomPartBurgerMenu = document.getElementById('bottomPartOfBurgerMenu')
	const navigation = document.getElementById('navigation')

	function openBurgerMenu() {
		burgerMenuIcon.classList.remove('visible')
		burgerMenuIcon.classList.add('not__visible')

		closeBurgerMenuIcon.classList.remove('not__visible')
		closeBurgerMenuIcon.classList.add('visible')

		bottomPartBurgerMenu.classList.remove('not__visible')
		bottomPartBurgerMenu.classList.add('visible')

    navigation.classList.add('background__white')
	}

  function closeBurgerMenu() {
		burgerMenuIcon.classList.remove('not__visible')
		burgerMenuIcon.classList.add('visible')

		closeBurgerMenuIcon.classList.remove('visible')
		closeBurgerMenuIcon.classList.add('not__visible')

		bottomPartBurgerMenu.classList.remove('visible')
		bottomPartBurgerMenu.classList.add('not__visible')

	}

	if (e.target?.id === 'burgerMenu') {
		openBurgerMenu()
	}
  if (e.target?.id === 'closeIcon' || 
			e.target?.id === 'bottomPartOfBurgerMenu') {
		closeBurgerMenu()
	}
})
