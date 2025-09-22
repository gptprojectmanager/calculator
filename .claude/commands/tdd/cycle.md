# TDD Cycle Command

Execute a complete Red-Green-Refactor cycle for test-driven development.

## Command
`/tdd:cycle`

## Description
Performs a full TDD cycle including:
1. **Red Phase**: Write failing tests
2. **Green Phase**: Implement minimal solution
3. **Refactor Phase**: Improve code quality

## Usage Context
- Use when starting a new feature or bug fix
- Integrates with CCPM issue tracking
- Maintains test coverage throughout development

## Prerequisites
- Requirements/specifications loaded (use `/pm:issue-start` first)
- Test framework configured (use `/testing:prime` if needed)

## Process
1. Analyzes current requirements/specifications
2. Generates comprehensive failing tests (Red)
3. Implements minimal code to pass tests (Green) 
4. Refactors for quality while maintaining tests (Refactor)
5. Updates issue progress if integrated with CCPM

## Integration with CCPM
- Automatically updates GitHub Issues with TDD progress
- Links test results to specifications
- Tracks coverage metrics in project reports

## Quality Gates
- All tests must pass before refactor phase
- Coverage threshold must be maintained
- No breaking changes to existing functionality