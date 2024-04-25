document.addEventListener('DOMContentLoaded', function () {
	const staging = document.querySelector('.staging')
	const sectionBanner = document.querySelector('.banner')

	if (!staging) return

  sectionBanner.classList.add('staging-fix')
})
