'use strict';

module.exports = function(grunt) {

    require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        project: {
            app: 'insegel',
            assets: '<%= project.app %>/static',
            css: [
                'scss/style.scss'
            ]
        },

        sass: {
            dev: {
                options: {
                    style: 'expanded'
                },
                files: {
                    '<%= project.assets %>/css/style.css': '<%= project.css %>'
                }
            },
            dist: {
                options: {
                    style: 'compressed',
                    sourcemap: 'none'
                },
                files: {
                    '<%= project.assets %>/css/style.css': '<%= project.css %>'
                }
            }
        },

        watch: {
            sass: {
                files: 'scss/{,*/}*.{scss,sass}',
                tasks: ['sass:dev']
            }
        }
    });

    grunt.registerTask('default', ['sass:dev', 'watch']);
    grunt.registerTask('dist', ['sass:dist']);
};