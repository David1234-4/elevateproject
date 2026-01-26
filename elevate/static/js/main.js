// Get elements
const loginBtn = document.getElementById('login-btn');
const loginModal = document.getElementById('login-modal');
const loginForm = document.getElementById('login-form');
const profileImage = document.getElementById('profile-image');
const editProfileBtn = document.getElementById('edit-profile-btn');

// Add event listeners
loginBtn.addEventListener('click', () => {
    loginModal.style.display = 'block';
});

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Add login logic here
    console.log(`Username: ${username}, Password: ${password}`);
    loginModal.style.display = 'none';
});

editProfileBtn.addEventListener('click', () => {
    // Add edit profile logic here
    console.log('Edit profile clicked');
});

// Profile image upload
profileImage.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
        document.getElementById('profile-image-preview').src = reader.result;
    };
    reader.readAsDataURL(file);
});

// Course enrollment
const enrollBtns = document.querySelectorAll('.enroll-btn');
enrollBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
        const courseId = btn.dataset.courseId;
        // Add course enrollment logic here
        console.log(`Enrolled in course ${courseId}`);
    });
});

// Progress bar animation
const progressBars = document.querySelectorAll('progress');
progressBars.forEach((bar) => {
    const value = bar.value;
    const max = bar.max;
    const percentage = (value / max) * 100;
    bar.style.background = `linear-gradient(to right, #007bff ${percentage}%, #ccc ${percentage}%)`;
});


// Posts Page JavaScript Code

// Add event listener to post titles
document.addEventListener('DOMContentLoaded', () => {
    const postTitles = document.querySelectorAll('.post-title a');
    postTitles.forEach((title) => {
        title.addEventListener('click', (e) => {
            e.preventDefault();
            const postId = title.dataset.postId;
            // Add logic to handle post click
            console.log(`Post ${postId} clicked`);
        });
    });
});

// Add event listener to pagination links
document.addEventListener('DOMContentLoaded', () => {
    const paginationLinks = document.querySelectorAll('.pagination a');
    paginationLinks.forEach((link) => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const pageNumber = link.dataset.pageNumber;
            // Add logic to handle pagination click
            console.log(`Page ${pageNumber} clicked`);
        });
    });
});
