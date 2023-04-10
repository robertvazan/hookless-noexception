// Part of Hookless: https://hookless.machinezoo.com
import com.machinezoo.stagean.*;

/**
 * Reactive extensions for <a href="https://noexception.machinezoo.com/">NoException</a>.
 * See {@link com.machinezoo.hookless.noexception.ReactiveExceptions}.
 * 
 * @see <a href="https://hookless.machinezoo.com/">Hookless website</a>
 */
@StubDocs
@NoTests
@DraftApi
module com.machinezoo.hookless.noexception {
	exports com.machinezoo.hookless.noexception;
	requires com.machinezoo.hookless;
	requires transitive com.machinezoo.noexception;
	requires com.machinezoo.stagean;
}
