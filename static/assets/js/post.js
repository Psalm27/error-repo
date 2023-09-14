document.getElementById("post-form").addEventListener("submit", function (e) {
    e.preventDefault();

    // Get values from form fields
    const jobTitle = document.getElementById("job-title").value;
    const requirements = document.getElementById("requirements").value;
    const responsibilities = document.getElementById("responsibilities").value;
    const deadline = document.getElementById("deadline").value;
    const salary = document.getElementById("salary").value;
    const course = document.getElementById("course").value;

    // You can perform further actions with the form data here, such as sending it to a server

    // For now, let's just log the data
    console.log("Job Title:", jobTitle);
    console.log("Requirements:", requirements);
    console.log("Responsibilities:", responsibilities);
    console.log("Deadline:", deadline);
    console.log("Salary:", salary);
    console.log("Course Required:", course);
});
