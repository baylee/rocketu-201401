var registrar = angular.module('registrar', ['ngRoute']);

registrar.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/views/index.html', controller: IndexCtrl}).
        when('/add/student/', {templateUrl: '/static/views/add_student.html', controller: AddStudentCtrl}).
        when('/add/project/', {templateUrl: '/static/views/add_project.html', controller: AddProjectCtrl}).
        otherwise({redirectTo: '/'});
}]);