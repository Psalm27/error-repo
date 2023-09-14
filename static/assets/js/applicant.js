// Get all "View" buttons
const viewButtons = document.querySelectorAll('.view-button');

// Add a click event listener to each "View" button
viewButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
        // In a real-world scenario, you would load applicant data dynamically.
        // For now, let's display a simple alert with the applicant's information.
        const applicants = [
            { name: 'John Doe', course: 'Computer Science', university: 'Example University' },
            { name: 'Jane Smith', course: 'Engineering', university: 'Another University' }
            // Add more applicant data as needed
        ];

        const applicant = applicants[index];
        if (applicant) {
            alert(`Applicant Information:\nName: ${applicant.name}\nCourse: ${applicant.course}\nUniversity: ${applicant.university}`);
        } else {
            alert('Applicant not found');
        }
    });
});
