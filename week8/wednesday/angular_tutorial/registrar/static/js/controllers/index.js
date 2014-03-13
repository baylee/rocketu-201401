function IndexCtrl($scope, $http) {
    $http.get('/api/v1/student/?format=json').
        success(function(students){
            $scope.students = students.objects;
        });
}