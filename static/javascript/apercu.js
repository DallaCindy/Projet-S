
document.addEventListener('DOMContentLoaded', function () {
    // Retrieve URL parameters
    const urlParams = new URLSearchParams(window.location.search);

    // Sample data from form (in a real application, this would come from the form submission)
    // For demonstration, we're using data passed via URL or hardcoded values
    const userData = {
        name: urlParams.get('user_name') || "{{user_name}}",
        age: parseInt(urlParams.get('user_age') || "{{user_age}}"),
        revenue: parseInt(urlParams.get('user_revenue') || "{{user_revenue}}"),

        // Categories selected (oui/non)
        logement: urlParams.get('logement') || "{{logement}}",
        alimentation: urlParams.get('alimentation') || "{{alimentation}}",
        transport: urlParams.get('transport') || "{{transport}}",
        sante: urlParams.get('sante') || "{{sante}}",
        epargnes: urlParams.get('epargnes') || "{{epargnes}}",

        // Priorities
        priorites_logement: urlParams.get('priorites_logement') || "{{priorites_logement}}",
        priorites_alimentation: urlParams.get('priorites_alimentation') || "{{priorites_alimentation}}",
        priorites_transport: urlParams.get('priorites_transport') || "{{priorites_transport}}",
        priorites_sante: urlParams.get('priorites_sante') || "{{priorites_sante}}",
        priorites_epargnes: urlParams.get('priorites_epargnes') || "{{priorites_epargnes}}",

        // Current expenses
        user_old_logement: parseInt(urlParams.get('user_old_logement') || "{{user_old_logement}}") || 0,
        user_old_alimentation: parseInt(urlParams.get('user_old_alimentation') || "{{user_old_alimentation}}") || 0,
        user_old_transport: parseInt(urlParams.get('user_old_transport') || "{{user_old_transport}}") || 0,
        user_old_sante: parseInt(urlParams.get('user_old_sante') || "{{user_old_sante}}") || 0,
        user_old_epargnes: parseInt(urlParams.get('user_old_epargnes') || "{{user_old_epargnes}}") || 0
    };

    // Fill user profile information
    document.getElementById('userName').textContent = userData.name;
    document.getElementById('userAge').textContent = userData.age;
    document.getElementById('userRevenue').textContent = formatCurrency(userData.revenue);
    document.getElementById('totalRevenue1').textContent = formatCurrency(userData.revenue);
    document.getElementById('totalRevenue2').textContent = formatCurrency(userData.revenue);

    // Calculate total current expenses
    const totalExpenses = calculateTotalExpenses(userData);
    document.getElementById('totalExpenses').textContent = formatCurrency(totalExpenses);

    // Calculate budget allocations
    const budgetRule5030 = calculateBudget(userData, { needs: 0.5, wants: 0.3, savings: 0.2 });
    const budgetRule7515 = calculateBudget(userData, { needs: 0.75, wants: 0.15, savings: 0.1 });

    // Update budget values
    document.getElementById('needs50').textContent = formatCurrency(budgetRule5030.needs);
    document.getElementById('wants30').textContent = formatCurrency(budgetRule5030.wants);
    document.getElementById('savings20').textContent = formatCurrency(budgetRule5030.savings);

    document.getElementById('needs75').textContent = formatCurrency(budgetRule7515.needs);
    document.getElementById('wants15').textContent = formatCurrency(budgetRule7515.wants);
    document.getElementById('savings10').textContent = formatCurrency(budgetRule7515.savings);

    // Generate chart segments
    generateChartSegments('chart1', [
        { percentage: 50, color: '#1a8755' },
        { percentage: 30, color: '#ffd700' },
        { percentage: 20, color: '#ff6b6b' }
    ]);

    generateChartSegments('chart2', [
        { percentage: 75, color: '#1a8755' },
        { percentage: 15, color: '#ffd700' },
        { percentage: 10, color: '#ff6b6b' }
    ]);

    // Generate budget details
    generateBudgetDetails(userData, budgetRule5030, 'budgetDetails1', '50-30-20');
    generateBudgetDetails(userData, budgetRule7515, 'budgetDetails2', '75-15-10');

    // Tab switching
    document.querySelectorAll('.tab-button').forEach(button => {
        button.addEventListener('click', function () {
            // Remove active class from all tabs
            document.querySelectorAll('.tab-button').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

            // Add active class to current tab
            this.classList.add('active');
            document.getElementById(this.dataset.tab).classList.add('active');
        });
    });

    // Toggle details
    document.getElementById('toggleDetails1').addEventListener('click', function () {
        toggleDetails('detailsSection1', this);
    });

    document.getElementById('toggleDetails2').addEventListener('click', function () {
        toggleDetails('detailsSection2', this);
    });

    // Download PDF (placeholder for actual functionality)
    document.getElementById('downloadPDF').addEventListener('click', function (e) {
        e.preventDefault();
        alert('La fonctionnalité de téléchargement en PDF sera bientôt disponible.');
    });
});

// Calculate total current expenses
function calculateTotalExpenses(userData) {
    return userData.user_old_logement +
        userData.user_old_alimentation +
        userData.user_old_transport +
        userData.user_old_sante +
        userData.user_old_epargnes;
}

// Format currency values
function formatCurrency(value) {
    return new Intl.NumberFormat('fr-FR', { style: 'currency', currency: 'EUR' }).format(value);
}

// Calculate budget allocations including category distribution
function calculateBudget(userData, rule) {
    const categories = [
        { id: 'logement', name: 'Logement', expense: userData.user_old_logement, isPriority: userData.priorites_logement === 'oui', isSelected: userData.logement === 'oui' },
        { id: 'alimentation', name: 'Alimentation', expense: userData.user_old_alimentation, isPriority: userData.priorites_alimentation === 'oui', isSelected: userData.alimentation === 'oui' },
        { id: 'transport', name: 'Transport', expense: userData.user_old_transport, isPriority: userData.priorites_transport === 'oui', isSelected: userData.transport === 'oui' },
        { id: 'sante', name: 'Santé', expense: userData.user_old_sante, isPriority: userData.priorites_sante === 'oui', isSelected: userData.sante === 'oui' },
        { id: 'epargnes', name: 'Épargne', expense: userData.user_old_epargnes, isPriority: false, isSelected: userData.epargnes === 'oui' }
    ];

    // Calculate total allocations
    const needsTotal = Math.round(userData.revenue * rule.needs);
    const wantsTotal = Math.round(userData.revenue * rule.wants);
    const savingsTotal = Math.round(userData.revenue * rule.savings);

    // Group categories
    const needsCategories = categories.filter(cat => cat.isSelected && cat.isPriority && cat.id !== 'epargnes');
    const wantsCategories = categories.filter(cat => cat.isSelected && !cat.isPriority && cat.id !== 'epargnes');
    const savingsCategories = categories.filter(cat => cat.id === 'epargnes' && cat.isSelected);

    // Calculate proportions for needs
    const needsSum = needsCategories.reduce((sum, cat) => sum + cat.expense, 0);
    needsCategories.forEach(cat => {
        cat.allocated = needsSum ? Math.round((cat.expense / needsSum) * needsTotal) : 0;
    });

    // Calculate proportions for wants
    const wantsSum = wantsCategories.reduce((sum, cat) => sum + cat.expense, 0);
    wantsCategories.forEach(cat => {
        cat.allocated = wantsSum ? Math.round((cat.expense / wantsSum) * wantsTotal) : 0;
    });

    // Savings allocation
    savingsCategories.forEach(cat => {
        cat.allocated = savingsTotal;
    });

    return {
        needs: needsTotal,
        wants: wantsTotal,
        savings: savingsTotal,
        categories: {
            needs: needsCategories,
            wants: wantsCategories,
            savings: savingsCategories
        }
    };
}

// Generate pie chart segments
function generateChartSegments(chartId, segments) {
    const chart = document.getElementById(chartId);
    let rotation = 0;

    segments.forEach(segment => {
        const slice = document.createElement('div');
        const percentage = segment.percentage;
        const color = segment.color;

        slice.className = 'chart-segment';
        slice.style.backgroundColor = color;
        slice.style.transform = `rotate(${rotation}deg)`;

        // Create inner clip for segments > 50%
        if (percentage > 50) {
            const innerSlice = document.createElement('div');
            innerSlice.className = 'chart-segment';
            innerSlice.style.backgroundColor = color;
            innerSlice.style.transform = 'rotate(180deg)';
            slice.appendChild(innerSlice);
        }

        // Calculate rotation for next segment
        const sliceRotation = (percentage / 100) * 360;
        rotation += sliceRotation;

        chart.appendChild(slice);
    });
}

// Generate budget details for each category
function generateBudgetDetails(userData, budgetData, containerId, ruleType) {
    const container = document.getElementById(containerId);
    const categories = budgetData.categories;

    // Create category cards for each group
    [categories.needs, categories.wants, categories.savings].forEach(group => {
        group.forEach(category => {
            const card = document.createElement('div');
            card.className = 'budget-category';

            // Calculate difference from previous amount
            const difference = category.allocated - category.expense;
            const diffClass = difference >= 0 ? 'positive' : 'negative';

            card.innerHTML = `
                <div class="category-header">
                    <div class="category-icon">${getCategoryIcon(category.id)}</div>
                    <div class="category-name">${category.name}</div>
                    ${category.isPriority ? '<div class="category-badge priority">Priorité</div>' : ''}
                </div>
                <div class="budget-amount">${formatCurrency(category.allocated)}</div>
                <div class="budget-allocation">
                    ${ruleType} répartition
                </div>
                <div class="comparison">
                    <div class="old-amount">${formatCurrency(category.expense)}</div>
                    <div class="diff-amount ${diffClass}">
                        ${difference >= 0 ? '+' : ''}${formatCurrency(difference)}
                        <i class="fas ${difference >= 0 ? 'fa-arrow-up' : 'fa-arrow-down'}"></i>
                    </div>
                </div>
            `;

            container.appendChild(card);
        });
    });
}

// Get category icons
function getCategoryIcon(categoryId) {
    const icons = {
        logement: '<i class="fas fa-home"></i>',
        alimentation: '<i class="fas fa-utensils"></i>',
        transport: '<i class="fas fa-car"></i>',
        sante: '<i class="fas fa-heart"></i>',
        epargnes: '<i class="fas fa-piggy-bank"></i>'
    };
    return icons[categoryId] || '<i class="fas fa-tag"></i>';
}

// Toggle details section
function toggleDetails(sectionId, button) {
    const section = document.getElementById(sectionId);
    const icon = button.querySelector('.fa-chevron-down');

    section.classList.toggle('active');
    icon.classList.toggle('fa-chevron-down');
    icon.classList.toggle('fa-chevron-up');
}