# Package Information

<https://documentation.neutrinos.com/articles/#!pulse-publication/validator-plugins-gcc>

A simple validation utility for Alpha UI Base that provides basic input validation methods for common use cases

### Package Information

- Name: alpha-module-validator
- Version: 1.0.0
- Description: Component validations for forms and data
- Exposed Name: validate

### Features

- Email Validation: Validate email format using regex
- Phone Validation: Validate 10-digit phone numbers
- Regex Validation: Custom regex pattern validation
- Numeric Validation: Minimum and maximum value checks
- Length Validation: String length validation (min/max)
- Date Validation: JSON Schema date format validation

### API Reference

#### Main Export: validate

The validate object provides basic validation methods for common input types

#### Core Methods

Email Validation

```javascript
// Validate email format
const isValidEmail = ap.validate.email('user@example.com');
// Returns: true

const invalidEmail = ap.validate.email('invalid-email');
// Returns: false
```

Phone Validation

```javascript
// Validate 10-digit phone number
const isValidPhone = ap.validate.phone('1234567890');
// Returns: true

const invalidPhone = ap.validate.phone('123-456-7890');
// Returns: false
```

Regex Validation

```javascript
// Validate with custom regex pattern
const isValid = ap.validate.regex('test123', /^[a-z]+\d+$/);
// Returns: true

// Validate with string regex
const isValidWithString = ap.validate.regex('test123', '^[a-z]+\d+$');
// Returns: true

// Invalid input will return false and log a warning
const invalid = ap.validate.regex('invalid', /^\d+$/);
// Returns: false, logs: "Invalid input, failed regex validation"
```

Numeric Validation

```javascript
// Check minimum value
const isAboveMin = ap.validate.minimum(15, 10);
// Returns: true

const isBelowMin = ap.validate.minimum(5, 10);
// Returns: false

// Check maximum value
const isBelowMax = ap.validate.maximum(15, 20);
// Returns: true

const isAboveMax = ap.validate.maximum(25, 20);
// Returns: false
```

Length Validation

```javascript
// Check minimum length
const hasMinLength = ap.validate.minLength('hello', 3);
// Returns: true

const tooShort = ap.validate.minLength('hi', 5);
// Returns: false

// Check maximum length
const hasMaxLength = ap.validate.maxLength('hello', 10);
// Returns: true

const tooLong = ap.validate.maxLength('very long string', 5);
// Returns: false
```

Date Validation

```javascript
// Validate JSON Schema date format (YYYY-MM-DDThh:mm:ssZ)
const isValidDate = ap.validate.date('2023-12-25T10:30:00Z');
// Returns: true

const invalidDate = ap.validate.date('2023-12-25');
// Returns: false
```

### Usage Examples

Basic Page Operations

```javascript
import { validate } from 'alpha-module-validator';

// Validate form fields
function validateForm(formData) {
  const errors = {};
  
  // Email validation
  if (!validate.email(formData.email)) {
    errors.email = 'Please enter a valid email address';
  }
  
  // Phone validation
  if (!validate.phone(formData.phone)) {
    errors.phone = 'Please enter a valid 10-digit phone number';
  }
  
  // Age validation
  if (!validate.minimum(formData.age, 18)) {
    errors.age = 'You must be at least 18 years old';
  }
  
  // Username length validation
  if (!validate.minLength(formData.username, 3)) {
    errors.username = 'Username must be at least 3 characters long';
  }
  
  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
}

// Usage
const formData = {
  email: 'user@example.com',
  phone: '1234567890',
  age: 25,
  username: 'john_doe'
};

const result = validateForm(formData);
console.log(result.isValid); // true
console.log(result.errors); // {}
```
