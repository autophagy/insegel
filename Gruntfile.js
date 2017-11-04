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
                    style: 'compressed'
                },
                files: {
                    '<%= project.assets %>/css/style.css': '<%= project.css %>'
                }
            }
        },

        shell: {
            build_docs: {
                command: '.venv/bin/python -msphinx -Ea doc doc/_build/html'
            }
        },

        connect: {
            server: {
                options: {
                    port: 8000,
                    base: 'doc/_build/html'
                }
            }
        },

        watch: {
            sass: {
                files: 'scss/{,*/}*.{scss,sass}',
                tasks: ['sass:dev', 'shell:build_docs']
            },
            html: {
                files: 'insegel/{,*/}*.{html, py, conf}',
                tasks: ['shell:build_docs']
            }
        }
    });

    grunt.registerTask('default', ['sass:dev', 'shell:build_docs', 'connect', 'watch']);
    grunt.registerTask('dist', ['sass:dist']);
};
