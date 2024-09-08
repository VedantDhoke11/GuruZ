function showSignup(type) {
    // Hide all forms
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('signupCustomerForm').style.display = 'none';
    document.getElementById('signupPanditForm').style.display = 'none';

    // Show the appropriate signup form
    if (type === 'customer') {
        document.getElementById('signupCustomerForm').style.display = 'block';
    } else if (type === 'pandit') {
        document.getElementById('signupPanditForm').style.display = 'block';
    } else {
        document.getElementById('loginForm').style.display = 'block';
    }
}



document.getElementById('paymentMethod').addEventListener('change', function() {
    // Hide all payment details sections
    document.getElementById('cardDetails').classList.add('hidden');
    document.getElementById('upiDetails').classList.add('hidden');
    document.getElementById('gpayDetails').classList.add('hidden');
    document.getElementById('walletDetails').classList.add('hidden');

    // Show the selected payment details section
    const method = this.value;
    if (method === 'card') {
        document.getElementById('cardDetails').classList.remove('hidden');
    } else if (method === 'upi') {
        document.getElementById('upiDetails').classList.remove('hidden');
    } else if (method === 'gpay') {
        document.getElementById('gpayDetails').classList.remove('hidden');
    } else if (method === 'wallet') {
        document.getElementById('walletDetails').classList.remove('hidden');
    }
});

document.getElementById('paymentForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the default way

    // Basic client-side validation
    const method = document.getElementById('paymentMethod').value;
    let valid = true;

    if (method === 'card') {
        const name = document.getElementById('name').value;
        const cardNumber = document.getElementById('cardNumber').value;
        const expiryDate = document.getElementById('expiryDate').value;
        const cvv = document.getElementById('cvv').value;
        if (!name || !cardNumber || !expiryDate || !cvv) {
            alert('Please fill in all card details.');
            valid = false;
        }
    } else if (method === 'upi') {
        const upiId = document.getElementById('upiId').value;
        if (!upiId) {
            alert('Please enter your UPI ID.');
            valid = false;
        }
    } else if (method === 'gpay') {
        const gpayNumber = document.getElementById('gpayNumber').value;
        if (!gpayNumber) {
            alert('Please enter your Google Pay number.');
            valid = false;
        }
    } else if (method === 'wallet') {
        const walletId = document.getElementById('walletId').value;
        if (!walletId) {
            alert('Please enter your Wallet ID.');
            valid = false;
        }
    }

    const amount = document.getElementById('amount').value;
    if (!amount) {
        alert('Please enter the amount.');
        valid = false;
    }

    if (valid) {
        // Process the payment with the selected method
        alert('Payment processed successfully! (Simulated)');
    }
});
