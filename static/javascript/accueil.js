// Main JavaScript for Harmoneo App
document.addEventListener('DOMContentLoaded', function () {
    // Elements
    const startApp = document.querySelector('.start-app');
    const container = document.querySelector('.container');
    const form = document.getElementById('budget-form');
    const btnNext = document.getElementById('Suivant');
    const btnPrevious = document.getElementById('Precedent');

    // All form sections
    const sections = document.querySelectorAll('.form-section');
    const progressSteps = document.querySelectorAll('.progress-step');

    // Current step tracker
    let currentStep = 1;
    const totalSteps = sections.length;

    // Initialize
    function init() {
        // Hide previous button on first step
        btnPrevious.style.display = 'none';

        // Set up form conditional logic
        setupFormLogic();

        // Set up priority selection limit
        setupPriorityLimit();
    }

    // Start application
    if (startApp && container) {
        startApp.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector('.welcome-screen').style.display = 'none';
            container.style.display = 'flex';
        });
    }

    // Show specific step
    function showStep(stepNumber) {

        if (stepNumber === 3) {
            enablePriorities();
        }

        // Hide all sections
        sections.forEach(section => {
            section.classList.remove('active');
        });

        // Show current section
        sections[stepNumber - 1].classList.add('active');

        // Update progress indicators
        updateProgress(stepNumber);

        // Show/hide previous button
        btnPrevious.style.display = stepNumber === 1 ? 'none' : 'flex';

        // Update next button text on last step
        if (stepNumber === totalSteps) {
            btnNext.querySelector('span').textContent = 'Terminer';
        } else {
            btnNext.querySelector('span').textContent = 'Suivant';
        }

        // Update current step
        currentStep = stepNumber;
    }

    // Update progress indicators
    function updateProgress(stepNumber) {
        progressSteps.forEach((step, index) => {
            // Remove all classes first
            step.classList.remove('active', 'completed');

            // Set active class for current step
            if (index + 1 === stepNumber) {
                step.classList.add('active');
            }

            // Set completed class for previous steps
            if (index + 1 < stepNumber) {
                step.classList.add('completed');
            }
        });
    }

    // Validate current step
    function validateStep(stepNumber) {
        let isValid = true;
        const currentSection = sections[stepNumber - 1];

        // Check required fields based on the current section
        switch (stepNumber) {
            case 1: // Profile section
                const name = currentSection.querySelector('#name');
                const age = currentSection.querySelector('#age');
                const revenue = currentSection.querySelector('#revenue');

                if (!name.value.trim()) {
                    highlightInvalid(name);
                    isValid = false;
                }

                if (!age.value || age.value <= 0) {
                    highlightInvalid(age);
                    isValid = false;
                }

                if (!revenue.value || revenue.value <= 0) {
                    highlightInvalid(revenue);
                    isValid = false;
                }
                break;

            case 2: // Categories section
                const categoryRadios = currentSection.querySelectorAll('input[type="radio"]:checked');
                const requiredGroups = ['logement', 'alimentation', 'transport', 'sante', 'epargnes'];

                requiredGroups.forEach(group => {
                    const groupRadios = currentSection.querySelectorAll(`input[name="${group}"]:checked`);
                    if (groupRadios.length === 0) {
                        const categoryItem = currentSection.querySelector(`input[name="${group}"]`).closest('.category-item');
                        categoryItem.classList.add('highlight-required');
                        isValid = false;
                    }
                });
                break;

            case 3: // Priorities section
                const priorityCheckboxes = currentSection.querySelectorAll('.priority-checkbox:checked');
                if (priorityCheckboxes.length !== 2) {
                    currentSection.querySelector('.priority-info').classList.add('highlight-warning');
                    isValid = false;
                }
                break;

            case 4: // Expenses section
                // This validation depends on which categories were selected previously
                const selectedCategories = getSelectedCategories();

                selectedCategories.forEach(category => {
                    if (category.selected === 'oui') {
                        const expenseInput = currentSection.querySelector(`#${category.name}-expense`);
                        if (expenseInput && (!expenseInput.value || expenseInput.value < 0)) {
                            highlightInvalid(expenseInput);
                            isValid = false;
                        }
                    }
                });
                break;
        }

        return isValid;
    }

    // Highlight invalid field
    function highlightInvalid(element) {
        element.classList.add('invalid');
        element.addEventListener('input', function () {
            element.classList.remove('invalid');
        }, { once: true });
    }

    // Get selected categories
    function getSelectedCategories() {
        return [
            { name: 'logement', selected: document.querySelector('input[name="logement"]:checked')?.value || 'non' },
            { name: 'alimentation', selected: document.querySelector('input[name="alimentation"]:checked')?.value || 'non' },
            { name: 'transport', selected: document.querySelector('input[name="transport"]:checked')?.value || 'non' },
            { name: 'sante', selected: document.querySelector('input[name="sante"]:checked')?.value || 'non' },
            { name: 'epargnes', selected: document.querySelector('input[name="epargnes"]:checked')?.value || 'non' }
        ];
    }

    // Set up form conditional logic (show/hide expense items based on category selection)
    function setupFormLogic() {
        const expenseItems = document.querySelectorAll('.expense-item');

        // Initially hide all expense items
        expenseItems.forEach(item => {
            item.style.display = 'none';
        });

        // Listen for changes on category selections
        document.querySelectorAll('input[type="radio"][value="oui"]').forEach(radio => {
            radio.addEventListener('change', () => {
                updateExpenseVisibility('expense-');
                updateExpenseVisibility('priorites-');
            });
        });

        document.querySelectorAll('input[type="radio"][value="non"]').forEach(radio => {
            radio.addEventListener('change', () => {
                updateExpenseVisibility('expense-');
                updateExpenseVisibility('priorites-');
            });
        });
    }

    // Update expense item visibility based on selected categories
    function updateExpenseVisibility(prefix = 'expense-') {
        const selectedCategories = getSelectedCategories();

        selectedCategories.forEach(category => {
            const expenseItem = document.getElementById(`${prefix + category.name}`);
            if (expenseItem) {
                expenseItem.style.display = category.selected === 'oui' ? 'flex' : 'none';

                // Clear value if category is deselected
                if (category.selected === 'non') {
                    const input = expenseItem.querySelector('input');
                    if (input) input.value = '';
                }
            }
        });
    }

    // Set up priority selection limit (max 2)
    function setupPriorityLimit() {
        const priorityCheckboxes = document.querySelectorAll('.priority-checkbox');

        priorityCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function () {
                const checked = document.querySelectorAll('.priority-checkbox:checked');

                if (checked.length > 2) {
                    this.checked = false;

                    // Show a feedback message
                    const priorityInfo = document.querySelector('.priority-info');
                    priorityInfo.classList.add('highlight-warning');

                    setTimeout(() => {
                        priorityInfo.classList.remove('highlight-warning');
                    }, 1500);
                }
            });
        });
    }

    function enablePriorities() {
        const cards = document.querySelector('.category-list.priority-list');
    }

    // Event listeners
    btnNext.addEventListener('click', function (e) {
        e.preventDefault();

        if (validateStep(currentStep)) {
            if (currentStep < totalSteps) {
                showStep(currentStep + 1);
            } else {
                // Submit the form on the last step
                form.submit();
            }
        }
    });

    btnPrevious.addEventListener('click', function (e) {
        e.preventDefault();
        if (currentStep > 1) {
            showStep(currentStep - 1);
        }
    });

    // Remove highlight on category items
    document.querySelectorAll('.category-item').forEach(item => {
        const radios = item.querySelectorAll('input[type="radio"]');
        radios.forEach(radio => {
            radio.addEventListener('change', function () {
                item.classList.remove('highlight-required');
            });
        });
    });

    // Initialize the app
    init();
});

// Add event listener to input fields to remove invalid state on focus
document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('input');

    inputs.forEach(input => {
        input.addEventListener('focus', function () {
            this.classList.remove('invalid');
        });
    });
});