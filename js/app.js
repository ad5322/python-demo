
let Person = {
    firstName:'Arun',
    lastName:'Deepak',
    building_No:'5/152, Kmarajar street',
    employeeId:1,
};

Person.firstName = 'Karan';
Person.age = 31;
console.log(Person.firstName)
console.log(Person['lastName'])
console.log('employeeId' in Person)
console.log('price' in Person)