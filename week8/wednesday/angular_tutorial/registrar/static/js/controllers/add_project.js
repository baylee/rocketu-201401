function AddProjectCtrl($scope, $http, $location) {
    $http.get('/api/v1/student/?format=json').
        success(function(students){
            $scope.students = students.objects;
        });

    $scope.submitForm = function() {
        $http.post('/api/v1/student_project/?format=json', $scope.project).
            success(function(response){
                $location.path("/");
            })
    }
}