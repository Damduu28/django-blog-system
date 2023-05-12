const toggler = document.querySelector('.toggle__icon')
const toggle_icon = document.querySelector('.toggle__icon .fa-bars')
const navbar = document.querySelector('.navbar')
const formInput = document.querySelectorAll('.form__wrapper input')
const formTextarea = document.querySelectorAll('.form__wrapper textarea')
const eyeIcon = document.querySelectorAll('.field__group .fa-eye')
const search_input = document.querySelector('.search__bar input')
const posts = document.getElementsByClassName('post')
const publish = document.querySelectorAll('.publish')

if (toggle_icon != null) {
    document.addEventListener('click', e => {
        let isIcon = e.target.matches('.fa-bars')
        if (isIcon) {
            toggle_icon.classList.toggle('fa-times')
            toggler.classList.toggle('active')
            navbar.classList.toggle('active')
        } else {
            toggler.classList.remove('active')
            navbar.classList.remove('active')
            toggle_icon.classList.remove('fa-times')
        }
    })
}

document.addEventListener('click', e => {
    let isDropdownBtn = e.target.matches('[data-dropdown-btn]')
    if (!isDropdownBtn && e.target.closest('[data-dropdown]') != null) return

    let currentDropdown
    if (isDropdownBtn) {
        currentDropdown = e.target.closest('[data-dropdown]')
        currentDropdown.classList.toggle('active')
    }

    document.querySelectorAll('[data-dropdown].active').forEach(dropdown => {
        if (dropdown === currentDropdown) return
        dropdown.classList.remove('active')
    });
})

formInput.forEach(input => {
    if (input.value !== '') {
        input.classList.add('active')
    } else {
        input.addEventListener('focus', e => {
            e.target.classList.add('active')
        })
    }
});

formInput.forEach(input => {
    input.addEventListener('blur', e => {
        if (e.target.value === '') {
            e.target.classList.remove('active')
        }
    })
});

formTextarea.forEach(text => {
    if (text.value !== '') {
        text.classList.add('active')
    } else {
        text.addEventListener('focus', e => {
            e.target.classList.add('active')
        })
    }
});

formTextarea.forEach(text => {
    text.addEventListener('blur', e => {
        if (e.target.value === '') {
            e.target.classList.remove('active')
        }
    })
});

eyeIcon.forEach(eye => {
    eye.addEventListener('click', e => {
        let passInput = e.target.nextElementSibling

        if (passInput.type === 'password') {
            passInput.type = 'text'
            e.target.classList.replace('fa-eye','fa-eye-slash')
        } else {
            passInput.type = 'password'
            e.target.classList.replace('fa-eye-slash','fa-eye')
        }
    })
});


if (search_input != null) {
    search_input.addEventListener('keyup', e => {
        let inputValue = e.target.value
        inputValue = inputValue.toLowerCase()

        for (let i = 0; i < posts.length; i++) {
            let title = posts[i].getElementsByClassName('post__name')[0];
            let titleValue = title.innerText || title.textContent
            titleValue = titleValue.toLowerCase()

            if (titleValue.indexOf(inputValue) > -1) {
                posts[i].style.display = ""
                console.log(posts.length)
            } else {
                posts[i].style.display = "none"
            }
        }
    })
}

publish.forEach(public => {
    let publicValue = public.dataset.status
    if (publicValue  === 'False') {
        public.innerText = "Publish"
        public.style.color = "green"
    }else if (publicValue === 'True') {
        public.innerText = "Unpublish"
        public.style.color = "red"
    }
});