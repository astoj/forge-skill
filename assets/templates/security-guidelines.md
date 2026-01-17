# Security Guidelines

## 1. Authentication
- Passwords hashed with bcrypt (cost >= 12)
- JWT tokens with appropriate expiry
- Refresh token rotation

## 2. Authorization
- RBAC implemented
- Resource ownership validation
- Audit logging for sensitive operations

## 3. Data Protection
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- PII handling procedures

## 4. Input Validation
- Server-side validation for all input
- Parameterized queries (no SQL injection)
- Output encoding (no XSS)

## 5. Security Headers
```
Strict-Transport-Security: max-age=31536000
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
```

## 6. Rate Limiting
| Endpoint Type | Limit |
|---------------|-------|
| Authentication | 5/minute |
| API | 100/minute |

## 7. Checklist
- [ ] No secrets in code
- [ ] Dependencies scanned
- [ ] Security headers configured
- [ ] Rate limiting enabled
